import Vue from "vue";
import {
  Alert,
  Input,
  Form,
  FormItem,
  Select,
  Option,
  DatePicker,
  Tabs,
  TabPane,
  Upload,
  Message,
  Button,
  Checkbox,
  Dialog,
  MessageBox,
  Progress,
  Notification,
  Carousel,
  CarouselItem,
  InputNumber,
} from "element-ui";

Vue.use(Checkbox);
Vue.use(Form);
Vue.use(Dialog);
Vue.use(InputNumber);
Vue.use(FormItem);
Vue.use(Input);
Vue.use(Select);
Vue.use(Option);
Vue.use(DatePicker);
Vue.use(Tabs);
Vue.use(TabPane);
Vue.use(Upload);
Vue.use(Button);
Vue.use(Progress);
Vue.use(Alert);
Vue.use(Carousel);
Vue.use(CarouselItem);

Vue.prototype.$message = Message;
Vue.prototype.$messageBox = MessageBox;
Vue.prototype.$notify = Notification;