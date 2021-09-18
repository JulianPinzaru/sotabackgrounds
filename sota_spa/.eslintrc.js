module.exports = {
	root: true,

	env: {
		node: true
	},

	parserOptions: {
		parser: 'babel-eslint'
	},

	rules: {
		'no-prototype-builtins': 0,
		'vue/require-v-for-key': 2,
		'linebreak-style': ['error', 'unix'],
		semi: ['error', 'always'],
		radix: ['error', 'always'],
		yoda: ['error'],
		'no-shadow': ['error'],
		'no-use-before-define': ['error'],
		'no-cond-assign': ['error', 'always'],
		'no-eval': ['error'],
		'no-eq-null': ['error'],
		'no-else-return': ['error'],
		'no-empty-function': ['error'],
		'no-extend-native': ['error'],
		'no-implicit-coercion': ['error'],
		'no-implicit-globals': ['error'],
		'no-implied-eval': ['error'],
		'no-invalid-this': ['warn'],
		'no-lone-blocks': ['error'],
		'no-loop-func': ['error'],
		'no-return-assign': ['error'],
		'no-script-url': ['error'],
		'no-self-compare': ['error'],
		'no-sequences': ['error'],
		'no-unmodified-loop-condition': ['error'],
		'no-unused-expressions': ['error'],
		'no-useless-return': ['error'],
		'no-multi-spaces': ['error'],
		'no-with': ['error'],
		'no-warning-comments': ['off'],
		'no-param-reassign': ['warn'],
		'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
		'no-alert': ['warn'],
		'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
		'array-element-newline': ['error', 'consistent'],
		'array-bracket-spacing': ['error', 'never'],
		'comma-dangle': ['error', 'never'],
		'block-spacing': ['error', 'always'],
		'brace-style': ['error', 'stroustrup', { allowSingleLine: true }],
		camelcase: 0,
		'comma-spacing': ['error'],
		'comma-style': 2,
		'computed-property-spacing': ['error', 'never'],
		'eol-last': ['error', 'always'],
		'func-call-spacing': ['error', 'never'],
		'function-paren-newline': ['error', 'never'],
		'key-spacing': 2,
		'no-lonely-if': 2,
		'no-mixed-operators': 2,
		'no-multiple-empty-lines': ['error', { max: 2, maxEOF: 0 }],
		'no-nested-ternary': 2,
		'no-trailing-spaces': 2,
		'space-in-parens': ['error', 'never'],
		'operator-linebreak': ['error', 'before'],
		'padded-blocks': ['error', 'never'],
		'vue/html-indent': ['error', 'tab'],
		'vue/no-unused-components': 0,
		'vue/script-indent': [
			'error',
			'tab',
			{
				baseIndent: 1,
				switchCase: 1,
				ignores: ['VAttribute']
			}
		],
		'vue/html-self-closing': 0,
		'vue/multiline-html-element-content-newline': 0,
		'vue/require-component-is': 0,

		'no-mixed-spaces-and-tabs': [
			'error',
			'smart-tabs'
		],
		indent: [2, 'tab'],
		'no-tabs': 0
	},

	overrides: [
		{
			files: ['*.vue'],
			rules: {
				indent: 'off'
			}
		}
	],

	globals: {
		_: 'readonly',
		$: 'readonly'
	},

	extends: [
		'plugin:vue/essential',
		'@vue/standard'
	]
};
