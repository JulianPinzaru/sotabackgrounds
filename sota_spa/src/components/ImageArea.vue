<template>
	<div class="image-area">
		<div class="image-wrapper">
			<img :src="image" />
			<v-icon class="image-icon-placeholder" x-large v-if="!image">mdi-image-outline</v-icon>
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
		// max-height: calc(100vh - 15.2rem) !important;

		.image-wrapper {
			display: flex;
			justify-content: center;
			width: 100%;
			height: 100%;
			position: relative;

			img {
				min-height: 50vh;
				// height: 100%;
				width: 100%;
				max-width: 1280px;
				max-height: 768px;
				object-fit: contain;
				object-position: center;
			}

			.image-icon-placeholder {
				position: absolute;
				z-index: 2;
				height: 100%;
			}
		}
	}
</style>
