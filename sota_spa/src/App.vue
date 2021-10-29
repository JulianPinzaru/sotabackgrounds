<template>
	<v-app color="blue-grey lighten-5">
		<main-app-bar />
		<nav-left />
		<nav-right />

		<v-main id="app-content" >
			<transition name="fade" appear mode="out-in">
				<router-view/>
			</transition>
		</v-main>
	</v-app>
</template>

<script>
	import MainAppBar from '@c/MainAppBar.vue';
	import NavLeft from '@c/NavLeft.vue';
	import NavRight from '@c/NavRight.vue';
	export default {
		name: 'App',
		components: {
			MainAppBar,
			NavLeft,
			NavRight
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
