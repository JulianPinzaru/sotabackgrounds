<template>
	<v-container fluid>
		<image-area :image="getDisplayedImage" />
		<div class="d-flex justify-center" id="generate-wrapper">
			<v-btn primary x-large block @click="generate">Generate</v-btn>
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
		justify-content: center;
		position: relative;
		height: 100%;
	}
	#generate-wrapper {
		position: absolute;
		bottom: 0;
		width: 100%;
	}
</style>
