import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import _ from 'lodash';
import axios_instance from './api.service';

import '@/styles/main.scss';

Vue.config.productionTip = false;

Vue.prototype.$http = axios_instance;
Vue.prototype.axios = axios_instance;

Vue.use(_);

new Vue({
	router,
	store,
	vuetify,
	render: h => h(App)
}).$mount('#app');
