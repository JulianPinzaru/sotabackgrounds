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
		display: flex;
		justify-content: center;
		align-items: top;
		.image-wrapper {
			width: 100%;
			height: calc(100vh - 15.2rem) !important;
			img {
				height: 100%;
				width: 100%;
				object-fit: contain;
				object-position: center;
			}
		}
	}
</style>
