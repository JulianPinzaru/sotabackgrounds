/* eslint camelcase: 0 */
/* eslint no-shadow: ["error", { "allow": ["state", "getters"] }] */

// import Vue from 'vue';

const state = {
	navLeft: false,
	navRight: false
};

const getters = {
};

const actions = {
};

const mutations = {
	openNavLeft (state) {
		state.navLeft = true;
	},
	openNavRight (state) {
		state.navRight = true;
	},
	toggleNavLeft (state) {
		state.navLeft = !state.navLeft;
	},
	toggleNavRight (state) {
		state.navRight = !state.navRight;
	}
};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};
