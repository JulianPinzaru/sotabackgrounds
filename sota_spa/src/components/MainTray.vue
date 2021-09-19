<template>
	<v-navigation-drawer id="main-tray" app clipped :value="isTrayOpened" width="320px">
		<v-list>
			<v-list-group
				:value="isGeneratedImagesOpened"
			>
				<template v-slot:activator>
					<v-list-item-title>Generated Images</v-list-item-title>
				</template>
				<p v-for="i in 100" :key="i" class="mx-6"> some image goes here</p>

			</v-list-group>

			<v-divider />

			<v-list-group
				:value="isSavedImagesOpened"
			>
				<template v-slot:activator>
					<v-list-item-title>Saved Images</v-list-item-title>
				</template>
				<p class="mx-6"> some image goes here</p>
			</v-list-group>
		</v-list>
	</v-navigation-drawer>
</template>
<script>
	export default {
		name: 'MainTray',
		data () {
			return {
				isTrayOpened: true,
				isGeneratedImagesOpened: true,
				isSavedImagesOpened: false,
				admins: [
					['Management', 'mdi-account-multiple-outline'],
					['Settings', 'mdi-cog-outline']
				],
				cruds: [
					['Create', 'mdi-plus-outline'],
					['Read', 'mdi-file-outline'],
					['Update', 'mdi-update'],
					['Delete', 'mdi-delete']
				]
			};
		}
	};
</script>
<style lang="scss">
	#main-tray {
		& > div {
			// @include soft-scroll();
		}
		// top: 32px !important;
	}
</style>
