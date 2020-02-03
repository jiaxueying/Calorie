// http://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    ecmaVersion: 6,
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true,
    },
  },
  env: {
    browser: false,
    node: true,
    es6: true,
  },
  // required to lint *.vue files
  plugins: [
    'vue',
  ],
  extends: [
    // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
    // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
    'plugin:vue/strongly-recommended',
    'standard',
  ],

  // add your custom rules here
  rules: {
    eqeqeq: ['error', 'smart'],
    'space-infix-ops': ['error'],
    semi: ['error', 'always'],
    'no-extra-semi': 'error',
    'brace-style': ['error', '1tbs', {
      allowSingleLine: true,
    }],
    'object-curly-spacing': 0,
    'space-before-function-paren': ['error', 'never'],
    'space-before-blocks': ['error', 'always'],
    'keyword-spacing': 'error',
    'space-in-parens': ['error', 'never'],
    'comma-dangle': ['error', 'always-multiline'],
    // allow paren-less arrow functions
    'arrow-parens': 0,
    // allow async-await
    'generator-star-spacing': 0,
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,

    'vue/no-parsing-error': ['error', {
      'x-invalid-end-tag': false,
    }],
    'vue/max-attributes-per-line': [2, {
      singleline: 1,
      multiline: {
        max: 1,
        allowFirstLine: false,
      },
    }],
    'vue/html-indent': ['error', 2, {
      attribute: 1,
      closeBracket: 0,
      alignAttributesVertically: true,
      ignores: [],
    }],
    'vue/html-closing-bracket-newline': ['error', {
      singleline: 'never',
      multiline: 'always',
    }],
    'vue/html-quotes': ['error', 'double'],
  },
  globals: {
    'uni': 'readonly',
    'wx': 'readonly',
  },
};
