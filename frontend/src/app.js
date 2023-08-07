import React, { Component, lazy } from "react";
import { Provider } from "react-redux";
import { configureStore } from "redux/Store";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import enJson from 'locales/en.json';
import jaJson from 'locales/ja.json';
import { createBrowserHistory } from "history";
import BlogLayout from 'layouts/BlogLayout';

const History = createBrowserHistory({ basename: "/" });

i18n.use(initReactI18next).init({
  resources: {
    en: { translation: enJson },
    ja: { translation: jaJson },
  },
  lng: 'ja',
  fallbackLng: 'ja',
  interpolation: { escapeValue: false },
});


export default class App extends Component {

  render() {
    return (
        <Provider store={configureStore()}>
          <BrowserRouter history={History}>
            <Routes>
              <Route path="*" element={<BlogLayout/>}/>
            </Routes>
          </BrowserRouter>
        </Provider>
    );
  }
}
