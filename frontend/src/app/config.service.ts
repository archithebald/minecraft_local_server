import { Injectable } from '@angular/core';
import * as configData from '../assets/config.json';

@Injectable({
  providedIn: 'root',
})
export class ConfigService {
  getApiBaseUrl() {
    return configData.API_BASE_URL;
  }

  getEndpoint(name: string) {
    return (configData.ENDPOINTS as any)[name];
  }

  buildUrl(endpoint: string) {
    return this.getApiBaseUrl() + this.getEndpoint(endpoint);
  }

  constructor() {}
}
