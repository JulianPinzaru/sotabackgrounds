<template>
	<v-container fluid>
		<image-area :image="getDisplayedImage" />
		<h1>Pick the preset:</h1>

		<div class="bottom-area">
			<div class="presets">
				<img class="mx-2" v-for="preset in 4" :key="preset" :src="'http://lorempixel.com/240/160/'" />
			</div>
			<div class="generate">
				<v-btn color="primary" x-large block @click="generate">Generate</v-btn>
			</div>
		</div>
	</v-container>
</template>

<script>
	import { mapActions, mapGetters } from 'vuex';
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
				]
			};
		},
		computed: {
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
		justify-content: start;
		position: relative;

		height: 100%;
		overflow: hidden;
	}
	.bottom-area {
		// position: absolute;
		// bottom: 0;
		min-height: 200px;
		width: 100%;
		.presets {
			display: flex;
			flex-wrap: nowrap;
			flex-direction: row;
			justify-content: center;
			margin-bottom: 1rem;
		}
		.generate {
			display: flex;
			width: 100%;
		}
	}
</style>
