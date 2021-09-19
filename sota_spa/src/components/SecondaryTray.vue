<template>
	<v-navigation-drawer id="secondary-tray" app clipped :value="isTrayOpened" right width="280px">
		<v-list>
			<v-list-group
				:value="isGeneratedImagesOpened"
			>
				<template v-slot:activator>
					<v-list-item-title>Generated Images</v-list-item-title>
				</template>
				<div v-for="i in 10" :key="i" class="mx-6">
					<img class="stored-image" :src="require('@/assets/test-gen-bg/' + i + '.png')" />
				</div>
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
		name: 'SecondaryTray',
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
	#secondary-tray {
		& > div {
			@include soft-scroll($width: 0.5, $color: map-get($blue-grey, 'lighten-4'));
		}

		.stored-image {
			object-position: center;
			object-fit: cover;
			max-width: 100%;
			max-width: 120px;
		}
	}
</style>
