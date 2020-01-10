import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-default/index.css';   // 默认主题
/*import '../static/css/theme-green/index.css'; */      // 浅绿色主题
import "babel-polyfill";
import $ from 'jquery';
import VueResource from 'vue-resource'
import  VueQuillEditor from 'vue-quill-editor'

Vue.use(VueQuillEditor);
Vue.use(VueResource);

Vue.use(ElementUI);
Vue.prototype.$axios = axios;
new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

export default{ //后端地址
    url: "http://167.179.78.178:9090"
}
