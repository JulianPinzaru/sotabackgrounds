<template>
	<div class="image-area">
		<div class="image-wrapper">
			<img :src="image" />
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

			img {
				min-height: 50vh;
				// height: 100%;
				width: 100%;
				max-width: 1280px;
				max-height: 768px;
				object-fit: contain;
				object-position: center;
			}
		}
	}
</style>
