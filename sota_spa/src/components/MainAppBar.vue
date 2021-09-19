<template>
	<v-app-bar
		id="main-app-bar"
		app
		color="blue darken-4"
		dark
		flat
		clipped-left
		clipped-right
		short
		dense
		max-height="32px"
		height="32px"
		extension-height="32px"
	>
	</v-app-bar>
</template>
<script>
	export default {
		name: 'MainAppBar'
	};
</script>
<style lang="scss">
	#main-app-bar + #main-tray {
		// top: 32px !important;
	}
</style>
