<template>
	<v-container fluid class="image-area">
		<img :src="image" />
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
		height:  100%;
		display: flex;
		justify-content: center;
		align-items: center;
		img {
			width: 1024px;
			height: 1024px;
			object-fit: contain;
			object-position: center;
		}
	}
</style>
