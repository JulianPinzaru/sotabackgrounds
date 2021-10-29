import Vue from 'vue';
import Vuex from 'vuex';

import System from 'Stores/System.js';
import ImageGenerators from 'Stores/ImageGenerators.js';

Vue.use(Vuex);

export default new Vuex.Store({
	strict: process.env.NODE_ENV !== 'production',
	modules: {
		imageGenerators: ImageGenerators,
		system: System
	}
});
