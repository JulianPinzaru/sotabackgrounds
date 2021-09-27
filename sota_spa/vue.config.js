const webpack = require('webpack'); 
const path = require('path');

// const ESLintPlugin = require('eslint-webpack-plugin');

function resolve (dir) {
	return path.join(__dirname, dir);
}

module.exports = {
	transpileDependencies: [
		'vuetify'
	],
	lintOnSave: true,
	configureWebpack: finalConfig => {
		finalConfig.plugins.push(new webpack.ProvidePlugin({ _: "lodash" }));
	},
	chainWebpack: config => {
		// --- define aliases ---
		config.resolve.alias.set('@c', resolve('src/components'));
		config.resolve.alias.set('Stores', resolve('src/store'));
		config.resolve.alias.set('ImageGenerators', resolve('store/ImageGenerators'));

		// --- make mixins and vars available to component scoped scss ---
		const types = ['vue-modules', 'vue', 'normal-modules', 'normal']
   		types.forEach(type => addStyleResource(config.module.rule('scss').oneOf(type)))

		if (process.env.NODE_ENV !== 'production') {
			// --- enabled eslint on webpack ---
			config.module.rule('eslint').use('eslint-loader').tap(options => {
				options.emitWarning = true;
				options.fix = true;
				return options;
			});
		}

		config.plugin('html').tap(args => {
			args[0].title = "Fake Backgrounds";
			return args;
		});
	},
	// devServer: {
	// 	proxy: {
	// 		'/model/': {
	// 			target: 'http://localhost:8000',
	// 			ws: true,
	// 			changeOrigin: true,
	// 			logLevel: 'debug',
	// 		}
	// 	}
	// }
};

function addStyleResource (rule) {
	// --- make mixins and vars available to component scoped scss ---
	rule.use('style-resource').loader('style-resources-loader').options({
		patterns: [
			path.resolve(__dirname, './src/styles/_mixins.scss'),
			path.resolve(__dirname, './src/styles/_variables.scss'),
		],
	})
}
