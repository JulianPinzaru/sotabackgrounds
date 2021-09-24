<template>
	<v-app>
		<main-app-bar />
		<main-tray />
		<secondary-tray />

		<v-main id="app-content">
			<transition name="fade" appear mode="out-in">
				<router-view/>
			</transition>
		</v-main>
	</v-app>
</template>

<script>
	import MainAppBar from '@c/MainAppBar.vue';
	import MainTray from '@c/MainTray.vue';
	import SecondaryTray from '@c/SecondaryTray.vue';
	export default {
		name: 'App',
		components: {
			MainAppBar,
			MainTray,
			SecondaryTray
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
