import axios from 'axios';

export const baseDomain = process.env.VUE_APP_BASE_DOMAIN;
export const baseApiUrl = process.env.VUE_APP_BASE_API_URL;

const axios_instance = axios.create({
	baseURL: baseApiUrl
});

export default axios_instance;
