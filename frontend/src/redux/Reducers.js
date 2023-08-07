import { combineReducers } from "redux";
import settings from "./settings/Reducer";
import routesReducer from './routes/Reducer';
import times from './times/Reducer';


const Reducers = combineReducers({
  settings,
  routesReducer,
  times,
});

export default Reducers;
