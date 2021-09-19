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
	},
	chainWebpack: config => {
		config.resolve.alias.set('@c', resolve('src/components'));

		if (process.env.NODE_ENV !== 'production') {
			// That's the way to alter existing rule configuration (not entirely replace it)
			config.module.rule('eslint').use('eslint-loader').tap(options => {
				options.emitWarning = true;
				options.fix = true;
				return options;
			});
		}
	}
};
