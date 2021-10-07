<template>
	<v-container fluid class="image-area">

		<div class="image-wrapper">
			<img :src="image" />
		</div>
	</v-container>
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
		width: 100%;
		height: calc(100% - 5.2rem) !important;
		display: flex;
		justify-content: center;
		align-items: center;
		.image-wrapper {
			max-width: 1024px;
			max-height: 1024px;
			img {
				height: 100%;
				width: 100%;
				object-fit: contain;
				object-position: center;
			}
		}
	}
</style>
