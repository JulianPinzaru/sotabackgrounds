<template>
	<v-container fluid>
		<template v-if="!isEditing">
			<image-area :image="getDisplayedImage" />
			<div class="bottom-area">
				<div class="generate btn-group">
					<v-btn-toggle
						rounded
					>
						<v-btn :disabled="!getDisplayedImage" x-medium @click="download">
							<v-icon dark>mdi-download</v-icon>
						</v-btn>
						<v-btn class="btn-generate" color="primary" x-medium @click="generate">
							<v-icon left dark>mdi-fingerprint</v-icon>
							Generate
							<v-icon right dark>mdi-fingerprint</v-icon>
						</v-btn>
						<v-btn x-medium @click="startEditing">
							<v-icon dark>mdi-palette</v-icon>
						</v-btn>
					</v-btn-toggle>
				</div>
			</div>
		</template>
		<image-editor :is-open="isEditing" :image="editingImage" :image-name="editingImageName" @close="stopEditing"/>

	</v-container>
</template>

<script>

	import { mapActions, mapGetters, mapState, mapMutations } from 'vuex';
	import ImageArea from '../components/ImageArea.vue';
	import ImageEditor from '../components/ImageEditor.vue';

	export default {
		name: 'Dashboard',

		components: {
			ImageEditor,
			ImageArea
		},

		data () {
			return {
				editingImage: null
			};
		},
		computed: {
			...mapState('imageGenerators', {
				requestParameters: 'requestParameters'
			}),
			...mapGetters('imageGenerators', {
				getDisplayedImage: 'getDisplayedImage'
			}),
			isEditing () {
				return this.editingImage !== null;
			},
			editingImageName () {
				return `edited-image-${this.requestParameters.network}-${this.requestParameters.truncation_psi}.png`;
			}
		},

		methods: {
			...mapMutations('imageGenerators', ['setEditingImage']),
			...mapActions('imageGenerators', [
				'generate'
			]),
			download () {
				var a = document.createElement('a');
				a.href = this.getDisplayedImage;
				a.download = `image-${this.requestParameters.network}-${this.requestParameters.truncation_psi}.png`;
				document.body.appendChild(a);
				a.click();
				document.body.removeChild(a);
			},
			startEditing () {
				this.editingImage = this.getDisplayedImage;
			},
			stopEditing () {
				this.editingImage = null;
			}
		}
	};
</script>

<style lang="scss" scoped>
	.container {
		display: flex;
		flex-direction: column;
		justify-content: flex-start;

		height: 100%;
		overflow: hidden;
	}
	.bottom-area {
		width: 100%;
		margin-top: 2rem;

		.generate {
			display: flex;
			justify-content: center;
			width: 100%;
		}
		.btn-generate {
			font-size: 1.2em;
			font-weight: bold;
			font-family: Roboto;
			i {
				font-size: 1.25em;
			}
		}
	}
</style>
