<template>
	<v-app color="blue-grey lighten-5">
		<main-app-bar />
		<main-tray />
		<secondary-tray />

		<v-main id="app-content" >
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
	// @import '~vuetify/src/styles/styles.sass';

	#app-content {
		// background-color: map-deep-get($colors, 'blue-grey', 'darken-3');
	}
</style>
