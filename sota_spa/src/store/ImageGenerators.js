/* eslint camelcase: 0 */
/* eslint no-shadow: ["error", { "allow": ["state", "getters"] }] */

// import Vue from 'vue';

const LIMIT_GENERATED_IMAGES = 30;
const MULTICLASS_NETWORKS = ['backgrounds_generator'];

const DEFAULT_REQUEST_PARAMETERS = Object.freeze({
	network: 'universe_generator',
	seeds: null,
	truncation_psi: 0.6,
	class_idx: null,
	noise_mode: 'random'
});

const state = {
	displayedImage: null,
	generatedImages: [],
	lockedImages: [],
	requestParameters: {
		network: 'universe_generator',
		seeds: null,
		truncation_psi: 0.6,
		class_idx: null,
		noise_mode: 'random'
	},
	isEditing: false,
	editingImage: null
};

const getters = {
	isClassIdxAllowed: (state) => {
		return MULTICLASS_NETWORKS.includes(state.requestParameters.network);
	},
	generatedImagesExceedLimit: (state) => (limit) => {
		return state.generatedImages.length > limit;
	},
	getDisplayedImage: (state) => {
		return state.editingImage ? state.editingImage : state.displayedImage;
	}
};

const actions = {

	generate ({ commit, state, getters, dispatch }) {
		if (state.isEditing || state.editingImage) { commit('stopEditing'); }
		return new Promise((resolve, reject) => {
			this._vm.axios.post('model/', state.requestParameters).then(response => {
				commit('addGeneratedImage', response.data.image);
				if (getters.generatedImagesExceedLimit(LIMIT_GENERATED_IMAGES)) {
					commit('removeLastGeneratedImage');
				}
				dispatch('setDisplayedImage', response.data.image);
				resolve(response.data.image);
			});
		});
	},

	setDisplayedImage ({ commit, state }, image) {
		if (state.isEditing) { commit('stopEditing'); }
		commit('setDisplayedImage', image);
	},

	startEditing ({ commit }, image) {
		commit('startEditing', image);
	},

	stopEditing ({ commit }) {
		commit('stopEditing');
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
		if (params.network === 'backgrounds_generator' && state.requestParameters.class_idx === null) { params.class_idx = 0; }
		state.requestParameters = _.extend({}, state.requestParameters, params);
	},
	resetRequestParameters (state) {
		state.requestParameters = DEFAULT_REQUEST_PARAMETERS;
	},
	startEditing (state, image) {
		if (state.isEditing) { return; }
		state.isEditing = true;
		state.editingImage = image;
	},
	stopEditing (state) {
		state.isEditing = false;
	},
	setEditingImage (state, image) {
		state.editingImage = image;
	}
};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};
