<template>
	<v-container fluid>
		<image-area :image="image" />
		<v-btn primary @click="generate">Generate</v-btn>
	</v-container>
</template>

<script>
	import ImageArea from '../components/ImageArea.vue';

	export default {
		name: 'Dashboard',

		components: {
			ImageArea
		},

		data () {
			return {
				image: null,
				requestParameters: {
					network: 'universe_generator',
					seeds: null,
					truncation_psi: -0.2,
					// class_idx: null,
					class_idx: 5,
					noise_mode: 'random'
				}
			};
		},
		mounted () {
			this.axios.get('model/').then((response) => {
				console.log(response.data);
			});
		},

		methods: {
			generate () {
				this.axios.post('model/', this.requestParameters).then(response => {
					this.image = response.data.image;
				});
			}
		}
	};
</script>
