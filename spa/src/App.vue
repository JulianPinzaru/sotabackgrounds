<template>
	<v-app>
		<v-app-bar
			app
			color="blue darken-4"
			dark
			flat
			max-height="32px"
		>

		</v-app-bar>

		<v-main>
			<router-view/>
		</v-main>
	</v-app>
</template>

<script>

	export default {
		name: 'App',

		data: () => ({
			//
		})
	};
</script>
