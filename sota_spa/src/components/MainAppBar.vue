<template>
	<v-app-bar
		id="main-app-bar"
		app
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
		<v-btn dark icon small @click="toggleNavLeft" class="mr-1">
			<v-icon small>mdi-cog</v-icon>
		</v-btn>
		<v-btn dark icon small @click="toggleNavRight">
			<v-icon small>mdi-image-multiple-outline</v-icon>
		</v-btn>
	</v-app-bar>
</template>
<script>
	import { mapMutations } from 'vuex';

	export default {
		name: 'MainAppBar',
		methods: {
			...mapMutations('system', {
				toggleNavLeft: 'toggleNavLeft',
				toggleNavRight: 'toggleNavRight',
				openNavLeft: 'openNavLeft',
				openNavRight: 'openNavRight'
			}),
			mounted () {
				if (!this.$vuetify.breakpoint.mobile) {
					this.openNavLeft();
					this.openNavRight();
				}
			}
		}
	};
</script>
<style lang="scss">
	#main-app-bar + #main-tray {
		// top: 32px !important;
	}
	#main-app-bar {
		button {
			max-height: 100%;
			position: relative;
			left: 0;
			&:nth-child(2) {
				left: auto;
				right: 0;
			}
		}
		& > :nth-child(2) {
			float: right;
		}
	}
</style>
