/* eslint camelcase: 0 */
/* eslint no-shadow: ["error", { "allow": ["state", "getters"] }] */

// import Vue from 'vue';

const LIMIT_GENERATED_IMAGES = 30;
const MULTICLASS_NETWORKS = ['backgrounds_generator'];

const state = {
	displayedImage: null,
	generatedImages: [],
	lockedImages: [],
	requestParameters: {
		network: 'universe_generator',
		seeds: null,
		truncation_psi: 0.4,
		class_idx: null,
		noise_mode: 'random'
	}
};

const getters = {
	isClassIdxAllowed: (state) => {
		return MULTICLASS_NETWORKS.includes(state.requestParameters.network);
	},
	generatedImagesExceedLimit: (state) => (limit) => {
		return state.generatedImages.length > limit;
	},
	getDisplayedImage: (state) => {
		return state.displayedImage;
	}
};

const actions = {

	generate ({ commit, state, getters }) {
		return new Promise((resolve, reject) => {
			this._vm.axios.post('model/', state.requestParameters).then(response => {
				commit('addGeneratedImage', response.data.image);
				if (getters.generatedImagesExceedLimit(LIMIT_GENERATED_IMAGES)) {
					commit('removeLastGeneratedImage');
				}
				commit('setDisplayedImage', response.data.image);
				resolve(response.data.image);
			});
		});
	}
};

const mutations = {
	setDisplayedImage (state, image) {
		state.displayedImage = image;
	},
	addGeneratedImage (state, image) {
		state.generatedImages.splice(0, 0, image);
	},
	removeLastGeneratedImage (state) {
		state.generatedImages.splice(state.generatedImages.length - 1, 1);
	},
	setRequestParameters (state, params) {
		state.requestParameters = _.extend({}, state.requestParameters, params);
	}
};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};
