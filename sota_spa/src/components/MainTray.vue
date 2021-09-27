<template>
	<v-navigation-drawer id="main-tray" app clipped :value="isTrayOpened" width="340px">
		<v-list>
			<v-list-item>
				<v-select
					:items="networkSelect"
					@input="$event => assignParams('network', $event)"
					label="Image Type"
					flat
				></v-select>
			</v-list-item>
			<v-list-item>
				<v-select
					:items="networkClassSelect"
					@input="$event => assignParams('class_idx', $event)"
					label="Image Subtype"
					flat
				></v-select>
			</v-list-item>

			<v-list-item>
				<v-select
					:items="noiseModeSelect"
					@input="$event => assignParams('noise_mode', $event)"
					label="Noise Mode"
					flat
				></v-select>
			</v-list-item>

			<v-list-item class="mt-7">

				<v-slider
					label="Truncation"
					hint="Truncation psi ψ = 1 means no truncation. ψ = 0 means no diversity (the entire latent space generates a single average image.Usable values are usually between 0.5 and 1."
					max="3"
					min="-3"
					step="0.01"
					thumb-label="always"
					:value="requestParameters.truncation_psi"
					@input="$event => assignParams('truncation_psi', $event)"
				></v-slider>
				<!-- 				<v-text-field
					:value="requestParameters.truncation_psi"
					@input="$event => assignParams('truncation_psi', $event)"
					:min="-3.0"
					:max="3.0"
					type="number"
				/> -->
			</v-list-item>
		</v-list>
	</v-navigation-drawer>
</template>
<script>
	import { mapMutations, mapGetters, mapState } from 'vuex';

	export default {
		name: 'MainTray',
		data () {
			return {
				isTrayOpened: true,
				networkSelect: [
					{
						header: 'Network to use'
					},
					{
						divider: true
					},
					{
						value: 'universe_generator',
						text: 'Universe Image Generator'
					},
					{
						value: 'backgrounds_generator',
						text: 'Abstract Backgrounds Generator'
					}
				],
				networkClassSelect: [
					{
						header: 'The category of abstract pictures to generate.'
					},
					{
						divider: true
					},
					{
						value: 0,
						text: 'Defocused Blur',
						hint: 'Background Defocused Abstract Blur'
					},

					{
						value: 1,
						text: 'Ink Shapeless',
						hint: 'Background Ink Shapeless'
					},
					{
						value: 2,
						text: 'Background Gradient',
						hint: 'Background Gradient'
					},
					{
						value: 3,
						text: 'Background Abstract Shapes',
						hint: 'Background Abstract Shapes'
					},
					{
						value: 4,
						text: 'Background Bubbles',
						hint: 'Background Bubbles'
					},
					{
						value: 5,
						text: 'Background Paint Shapeless',
						hint: 'Background Paint Shapeless'
					},
					{
						value: 6,
						text: 'Background Geometry',
						hint: 'Background Geometry'
					}
				],
				noiseModeSelect: [
					{
						header: 'The amount of noise'
					},
					{
						divider: true
					},
					{
						value: 'const',
						text: 'Constant noise',
						hint: 'The image will look always the same if generated with the same noise'
					},
					{
						value: 'random',
						text: 'Random Noise',
						hint: 'Always generates slightly modified images for the same seed used.'
					},
					{
						value: 'none',
						text: 'No noise',
						hint: 'The algorithm won\'t use any noise parameters when generating the image.'
					}
				]

			};
		},
		computed: {
			...mapGetters('imageGenerators', ['isClassIdxAllowed']),
			...mapState('imageGenerators', ['requestParameters'])
		},
		methods: {
			...mapMutations('imageGenerators',
				['setRequestParameters']),

			assignParams (field, data) {
				this.setRequestParameters({ [field]: data });
			}
		}
	};
</script>
<style lang="scss">
	#main-tray {
		& > div {
			@include soft-scroll($width: 0.5, $color: map-get($blue-grey, 'lighten-4'));
		}
	}
</style>
