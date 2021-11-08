<template>
	<div class="image-area">
		<div :class="{'is-loading': isLoading, 'image-wrapper': true}">

			<div class="image-bg" :style="{'background-image': `url('${image}')`}" ></div>

			<v-icon class="image-icon-placeholder" x-large v-if="!image">mdi-image-outline</v-icon>
			<div class="image-loading" >
				<v-progress-circular
					v-if="isLoading"
					:size="70"
					:width="7"
					color="white"
					indeterminate
				></v-progress-circular>
			</div>
		</div>

	</div>
</template>

<script>
	export default {
		name: 'ImageArea',
		props: {
			image: {
				type: String,
				default: null,
				required: false
			},
			isLoading: {
				type: Boolean,
				default: false
			}
		},

		data: () => ({
		})
	};
</script>

<style scoped lang="scss">
	.image-area {
		display: flex;
		justify-content: center;
		align-items: flex-start;
		margin-top: 2rem;
		width: 100%;
		height: 100%;
		position: relative;

		.image-wrapper {
			display: flex;
			justify-content: center;
			width: 100%;
			height: 100%;
			position: relative;

			.image-bg, img {
				min-height: 50vh;
				// height: 100%;
				width: 100%;
				max-width: 1280px;
				max-height: 768px;
				object-fit: contain;
				object-position: center;
				background-position: center center;
				background-size: contain;
			}

			.image-icon-placeholder {
				position: absolute;
				z-index: 2;
				height: 100%;
			}

			&.is-loading {
				.image-bg, img {
					filter: blur(2px);
					transition: blur .2s ease-in;
				}
			}
		}
		.image-loading {
			position: absolute;
			top: 0; left: 0; right: 0; bottom: 0;
			width: 100%; height: 100%;
			display: flex;
			justify-content: center;
			align-items: center;
			z-index: 2;
		}
	}
</style>
