<template>
	<v-container>
		<panel-area />
		<image-area />
	</v-container>
</template>

<script>
	import PanelArea from '../components/PanelArea.vue';
	import ImageArea from '../components/ImageArea.vue';

	export default {
		name: 'Dashboard',

		components: {
			PanelArea,
			ImageArea
		}
	};
</script>
