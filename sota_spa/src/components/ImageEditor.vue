<template>
	<v-dialog
		v-model="dialog"
		fullscreen
		hide-overlay
		transition="scale-transition"
	>
		<v-btn
			class="close-image-editor"
			icon
			dark
			@click="closeEditor"
		>
			<v-icon>mdi-close</v-icon>
		</v-btn>

		<tui-image-editor v-if="editingImage" ref="tui-image-editor" :include-ui="includeUI" :options="options"></tui-image-editor>
	</v-dialog>
</template>

<script>
	import 'tui-color-picker/dist/tui-color-picker.css';
	import 'tui-image-editor/dist/tui-image-editor.css';
	import ImageEditor from '@toast-ui/vue-image-editor/src/ImageEditor.vue';

	export default {
		name: 'ImageEditor',
		props: {
			isOpen: {
				type: Boolean,
				default: false,
				required: false
			},
			image: {
				type: String,
				default: null,
				required: false
			},
			imageName: {
				type: String,
				default: 'default.jpg',
				required: false
			}
		},
		components: {
			'tui-image-editor': ImageEditor
		},

		data: () => ({
			localImage: null,
			dialog: false,
			notifications: false,
			sound: true,
			widgets: false,
			includeUI: true,
			options: {
				cssMaxWidth: 1280,
				cssMaxHeight: 768,
				includeUI: {
					loadImage: {
						path: null,
						name: 'default.jpg'
					}
				}
			}
		}),

		computed: {
			editingImage: {
				get () {
					return this.localImage;
				},
				set (newVal) {
					this.localImage = newVal;
				}
			}
		},

		watch: {
			isOpen (newVal) {
				this.dialog = newVal || false;
			},
			image (newVal, oldVal) {
				this.editingImage = newVal;
				if (newVal) {
					this.initEditor();
				}
			}
		},

		methods: {
			initEditor () {
				this.options.includeUI.loadImage.path = this.editingImage;
				this.options.includeUI.loadImage.name = this.imageName;
			},
			closeEditor () {
				this.$emit('close', this.editingImage);
			}
		}
	};
</script>

<style scoped lang="scss">
	.image-editor {
		width: 100%;
		height: 100%;
	}

	.close-image-editor {
		position: absolute;
		left: .2rem;
		top: .2rem;
		z-index: 2;
	}
</style>
