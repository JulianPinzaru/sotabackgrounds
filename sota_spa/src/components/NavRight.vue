<template>
	<v-navigation-drawer id="right-nav" app clipped :value="navRight" right width="280px">
		<v-list>
			<v-list-group
				:value="isGeneratedImagesOpened"
			>
				<template v-slot:activator>
					<v-list-item-title>Generated Images</v-list-item-title>
				</template>
				<v-item-group class="d-flex flex-row flex-wrap justify-center align-center">
					<div v-for="(img, idx) in generatedImages" :key="idx" class="mx-2">
						<v-item v-slot="{ active, toggle }">
							<img :class="{'stored-image': true, 'is-active': active}" :src="img" @click="select(img, toggle)"/>
						</v-item>
					</div>
				</v-item-group>
			</v-list-group>

			<v-divider />
		</v-list>
	</v-navigation-drawer>
</template>
<script>
	import { mapState, mapMutations } from 'vuex';
	export default {
		name: 'NavRight',
		data () {
			return {
				isTrayOpened: true,
				isGeneratedImagesOpened: true
			};
		},
		computed: {
			...mapState('imageGenerators', {
				generatedImages: 'generatedImages'
			}),
			...mapState('system', ['navRight'])
		},
		methods: {
			...mapMutations('imageGenerators', {
				setDisplayedImage: 'setDisplayedImage'
			}),
			select (image, toggleFunc) {
				this.setDisplayedImage(image);
				toggleFunc();
			}
		}
	};
</script>
<style lang="scss">
	#right-nav {
		& > div {
			@include soft-scroll($width: 0.5, $color: map-get($blue-grey, 'lighten-4'));
		}

		.stored-image {
			object-position: center;
			object-fit: cover;
			max-width: 100%;
			max-width: 80px;
			&:hover {
				cursor: pointer;
			}

			&.is-active {
				filter: brightness(150%);
			}
		}
	}
</style>
