<template>
	<v-navigation-drawer id="left-nav" app clipped :value="navLeft" width="280px" bottom>
		<v-list>
			<v-list-item>
				<v-select
					:items="networkSelect"
					:value="requestParameters.network"
					@input="$event => assignParams('network', $event)"
					label="Image Type"
					flat
				></v-select>
			</v-list-item>
			<v-list-item v-if="isClassIdxAllowed">
				<v-select
					:items="networkClassSelect"
					:value="requestParameters.class_idx"
					@input="$event => assignParams('class_idx', $event)"
					label="Image Subtype"
					flat
				></v-select>
			</v-list-item>

			<v-list-item>
				<v-select
					:items="noiseModeSelect"
					:value="requestParameters.noise_mode"
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
			</v-list-item>
			<v-list-item class="mt-3">
				<v-checkbox
					v-model="randomSeed"
					label="Use a random seed"
				></v-checkbox>
			</v-list-item>
			<v-list-item v-if="!randomSeed" class="mt-3">
				<v-text-field
					type="number"
					label="Specified seed number"
					:value="seed"
					@input="$event => seed = Number($event)"
					append-outer-icon="mdi-plus"
					@click:append-outer="incrementSeed"
					prepend-icon="mdi-minus"
					@click:prepend="decrementSeed"
					:max="65536"
					:min="0"
					:rules="[
						v => ( v >= 0 ) || 'The seed number cannot be negative.',
						v => ( v <= 65536 ) || 'The seed number cannot be above 65536.'
					]
					"
				>
				</v-text-field>
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
			...mapState('imageGenerators', ['requestParameters']),
			...mapState('system', ['navLeft']),
			seed: {
				get () {
					return !_.isEmpty(this.requestParameters.seeds) ? this.requestParameters.seeds[0] : null;
				},
				set (newVal) {
					if (newVal === null) { this.setRequestParameters({ seeds: null }); }
					else { this.setRequestParameters({ seeds: [newVal] }); }
				}
			},
			randomSeed: {
				get () {
					return this.seed === null;
				},
				set (newVal) {
					console.log(newVal);
					if (newVal === false) { this.seed = 0; }
					else { this.seed = null; }
				}
			}
		},
		methods: {
			...mapMutations('imageGenerators',
				['setRequestParameters']),

			assignParams (field, data) {
				this.setRequestParameters({ [field]: data });
			},

			incrementSeed () {
				this.seed = this.seed + 1;
			},

			decrementSeed () {
				this.seed = this.seed - 1;
			}
		}
	};
</script>
<style lang="scss">
	#left-nav {
		& > div {
			@include soft-scroll($width: 0.5, $color: map-get($blue-grey, 'lighten-4'));
		}
	}
</style>
