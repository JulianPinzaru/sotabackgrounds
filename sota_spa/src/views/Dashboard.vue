<template>
	<v-container fluid>
		<image-area :image="getDisplayedImage" />
		<v-btn primary @click="generate">Generate</v-btn>
	</v-container>
</template>

<script>
	import { mapActions, mapState, mapGetters } from 'vuex';
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
					truncation_psi: 0.4,
					class_idx: null,
					// class_idx: 4,
					noise_mode: 'random'
				}
			};
		},
		computed: {
			...mapState('imageGenerators', {
				generatedImages: 'generatedImages',
				lockedImages: 'lockedImages'
			}),
			...mapGetters('imageGenerators', {
				getDisplayedImage: 'getDisplayedImage'
			})
		},
		mounted () {
			// this.axios.get('model/').then((response) => {
			// 	console.log(response.data);
			// });
		},

		methods: {
			...mapActions('imageGenerators', {
				generate: 'generate'
			})
			// generate () {
			// 	this.axios.post('model/', this.requestParameters).then(response => {
			// 		this.image = response.data.image;
			// 	});
			// }
		}
	};
</script>
