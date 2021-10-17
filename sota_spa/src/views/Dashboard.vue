<template>
	<v-container fluid>
		<image-area :image="getDisplayedImage" />
		<h1>Pick the preset:</h1>
		<div class="">
			<img class="mx-2" v-for="preset in 4" :key="preset" :src="'http://lorempixel.com/240/160/'" />
		</div>
		<div class="d-flex justify-center" id="generate-wrapper">
			<v-btn color="primary" x-large block @click="generate">Generate</v-btn>
		</div>
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
				presets: [
					{
						image: ''
					}
				],
				image: null,
				requestParameters: {
					network: 'universe_generator',
					seeds: null,
					truncation_psi: 0.4,
					class_idx: null,
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

		methods: {
			...mapActions('imageGenerators', {
				generate: 'generate'
			})
		}
	};
</script>

<style lang="scss" scoped>
	.container {
		display: flex;
		flex-direction: column;
		justify-content: top;
		position: relative;

		height: 100%;
		max-height: calc(100vh - 1rem);
		overflow: hidden;
	}
	#generate-wrapper {
		position: absolute;
		bottom: 0;
		width: 100%;
	}
</style>
