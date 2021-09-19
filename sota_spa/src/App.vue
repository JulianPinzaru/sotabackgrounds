<template>
	<v-app>
		<main-app-bar />
		<main-tray />

		<v-main id="app-content">
			<router-view/>
		</v-main>
	</v-app>
</template>

<script>
	import MainAppBar from '@c/MainAppBar.vue';
	import MainTray from '@c/MainTray.vue';
	export default {
		name: 'App',
		components: {
			MainAppBar,
			MainTray
		},
		data: () => ({
			//
		})
	};
</script>
<style lang="scss">
	#app-content {
		// padding-top: 32px !important;
	}
</style>
