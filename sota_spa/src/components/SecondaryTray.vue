<template>
	<v-navigation-drawer id="secondary-tray" app clipped :value="isTrayOpened" right width="280px">
		<v-list>
			<v-list-group
				:value="isGeneratedImagesOpened"
			>
				<template v-slot:activator>
					<v-list-item-title>Generated Images</v-list-item-title>
				</template>
				<div v-for="(img, idx) in generatedImages" :key="idx" class="mx-6">
					<img class="stored-image" :src="img" @click="setDisplayedImage(img)"/>
				</div>
			</v-list-group>

			<v-divider />

			<v-list-group
				:value="isSavedImagesOpened"
			>
				<template v-slot:activator>
					<v-list-item-title>Saved Images</v-list-item-title>
				</template>
				<p class="mx-6"> some image goes here</p>
			</v-list-group>
		</v-list>
	</v-navigation-drawer>
</template>
<script>
	import { mapState, mapMutations } from 'vuex';
	export default {
		name: 'SecondaryTray',
		data () {
			return {
				isTrayOpened: true,
				isGeneratedImagesOpened: true,
				isSavedImagesOpened: false
			};
		},
		computed: {
			...mapState('imageGenerators', {
				generatedImages: 'generatedImages'
			})
		},
		methods: {
			...mapMutations('imageGenerators', {
				setDisplayedImage: 'setDisplayedImage'
			})
		}
	};
</script>
<style lang="scss">
	#secondary-tray {
		& > div {
			@include soft-scroll($width: 0.5, $color: map-get($blue-grey, 'lighten-4'));
		}

		.stored-image {
			object-position: center;
			object-fit: cover;
			max-width: 100%;
			max-width: 120px;
		}
	}
</style>
