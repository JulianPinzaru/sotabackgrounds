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

		<v-btn
			class="download-image"
			:icon="$vuetify.breakpoint.mobile ? true : false"
			:dark="$vuetify.breakpoint.mobile ? true : false"
			:color="$vuetify.breakpoint.mobile ? '' : 'primary'"
			:rounded="$vuetify.breakpoint.mobile ? '' : true"
			@click="downloadImage"
		>
			<v-icon v-if="$vuetify.breakpoint.mobile">mdi-download</v-icon>
			<template v-else>
				Download
			</template>
		</v-btn>
		<tui-image-editor v-if="editingImage" ref="tuiImageEditor" :include-ui="includeUI" :options="options"></tui-image-editor>
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

		mounted () {
			if (this.$vuetify.breakpoint.mobile) {
				this.options.cssMaxWidth = 360;
				this.options.cssMaxHeight = 470;
			}
		},

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
			},
			downloadImage () {
				const imgData = this.$refs.tuiImageEditor.invoke('toDataURL');
				var a = document.createElement('a');
				a.href = imgData;
				a.download = 'edited-image.png';
				document.body.appendChild(a);
				a.click();
				document.body.removeChild(a);
			}
		}
	};
</script>

<style lang="scss">
	@import '~vuetify/src/styles/styles.sass';

	.v-dialog {
		.image-editor {
			width: 100%;
			height: 100%;
		}

		.close-image-editor {
			position: absolute;
			left: .2rem;
			top: .2rem;
			z-index: 2;
			@include media-breakpoint('md-and-down') {
				top: 3.2rem;
				left: 0;
			}
		}
		.download-image {
			position: absolute;
			top: 3.2rem;
			right: 0;
			z-index: 2;
			@include media-breakpoint('md-and-up') {
				top: .8rem;
				right: .8rem;
				width: 120px;
				font-family: Roboto;
				text-transform: capitalize;
			}
		}

		// override tui styles
		.tui-image-editor-header-logo {
			display: none;
		}
		.tui-image-editor-header-buttons div:first-child {
			display: none;
		}
		.tui-image-editor-download-btn {
			background-color: var(--v-primary-base) !important;
			border-color: var(--v-primary-base) !important;
			display: none !important;
		}
		.tui-image-editor-download-btn {
			position: relative;
			top: 2.75rem;
			right: 1rem;
		}
		.tui-image-editor-container {
			background-color: map-get($material-dark-elevation-colors, '2');
			.tui-image-editor-main-container {
				background-color: map-get($material-dark-elevation-colors, '2') !important;
			}
			.tui-image-editor-controls {
				background-color: map-get($material-dark-elevation-colors, '1') !important;
			}
		}
		.tui-image-editor-submenu-style {
			background-color: map-get($material-dark-elevation-colors, '3') !important;
		}
	}


</style>
