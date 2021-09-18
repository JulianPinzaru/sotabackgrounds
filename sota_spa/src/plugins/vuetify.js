import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/es5/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
	customVariables: ['~/assets/styles/vuetify-override-variables.scss'],
	treeShake: true,
	// disables all the assets that are imported by default in vuetify
	// such as Roboto fonts (which you might not need), icons etc...
	defaultAssets: false,
	// alternative way is to use some of the customizations below
	// defaultAssets: {
	// 	font: {
	// 		family: ['Roboto:100,700&display=swap']
	// 	}
	// },
	icons: {
		iconfont: 'mdiSvg'
	},
	theme: {
		options: { customProperties: true },
		dark: false,
		themes: {
			light: {
				primary: colors.purple.darken1,
				secondary: colors.red.darken4,
				accent: colors.pink.lighten1,
				info: colors.teal.lighten1,
				warning: colors.amber.base,
				error: colors.deepOrange.accent4,
				success: colors.green.accent3,
				light_blue_section: '#F4F4F8'
				// light_blue_section_darken: '#e5e5f7'
			},
			dark: {
				primary: colors.pink.lighten1,
				accent: colors.purple.lighten1,
				secondary: colors.blue.lighten5,
				info: colors.teal.lighten1,
				warning: colors.amber.base,
				error: colors.deepOrange.accent4,
				success: colors.green.accent3
				// light_blue_section: '#F4F4F8',
				// light_blue_section_darken: '#e5e5f7'
			}
		}
	}
});
