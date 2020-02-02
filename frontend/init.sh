#!/bin/bash
echo -e "\033[32mSetting githook\033[0m\n"
cp ../pre-commit ../.git/hooks/
chmod 777 ../.git/hooks/pre-commit

which npm &> /dev/null
if [[ $? == 1 ]]; then
  echo -e "\033[32mPlease install npm\033[0m"
  exit 1
else
  echo -e "\033[32mDetected npm\033[0m\n"
fi

which cnpm &> /dev/null
if [[ $? == 1 ]]; then
  echo -e "\033[32minstalling cnpm\033[0m\n"
  npm install -g cnpm --registry=https://registry.npm.taobao.org
else
  echo -e "\033[32mDetected cnpm\033[0m\n"
fi
echo -e "\033[32mInstalling Vue.js\033[0m\n"
cnpm install -g @vue/cli @vue/cli-init
echo -e "\033[32mInstalling ESLint\033[0m\n"
cnpm install -g eslint@5.16.0 eslint-plugin-vue@5.2.3 eslint-config-standard eslint-plugin-standard eslint-plugin-promise eslint-plugin-import eslint-plugin-node
echo -e "\033[32mInstalling stylelint\033[0m\n"
cnpm install -g stylelint stylelint-config-standard stylelint-order stylelint-processor-html stylelint-webpack-plugin
echo -e "\033[32mInstalling frontend test tool\033[0m\n"
cnpm install -g jest istanbul
echo -e "\033[32mInstalling Project ESLint\033[0m\n"
cnpm install
