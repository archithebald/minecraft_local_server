import { Component, Input, OnChanges, OnInit, SimpleChange, SimpleChanges } from '@angular/core';
import { defaultUrlMatcher, Router, RouterOutlet } from '@angular/router';
import { ServerPageComponent } from '../server-page/server-page.component';
import { ServerPageLeftComponent } from '../server-page-left/server-page-left.component';
import { CommonModule, NgFor } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ConfigService } from '../config.service';
import { endWith } from 'rxjs';
import { FormsModule } from '@angular/forms';
import { fakeAsync } from '@angular/core/testing';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-server-options-page',
  standalone: true,
  imports: [RouterOutlet, ServerPageLeftComponent, CommonModule, HttpClientModule, FormsModule, MatIconModule],
  templateUrl: './server-options-page.component.html',
  styleUrl: './server-options-page.component.css',
})
export class ServerOptionsPageComponent implements OnInit {
  protected game_version: string | null = null;
  protected server_version: string | null = null;
  protected server_id: string | null = null;
  protected adress: string | null = null;
  protected description: string | null = null;
  protected properties: any = {};
  protected filtered_properties: any = {};
  private server: any = {};
  protected changedProperties: any = {};
  public search_query: string = "";

  ngOnInit(): void {
    this.setProperties();
    localStorage.clear();
  }

  unsavedChanges() {
    return Object.keys(this.changedProperties).length > 0;
  }

  setProperties() {
    var url = this.config.buildUrl("get_server_properties") + `?id=${this.server_id}`;

    this.http.get(url).subscribe((response: any) => {
      if (response.data == "null") {
        this.properties = null;
        this.filtered_properties = null;
      } else {
        this.properties = response.data;
        this.filtered_properties = this.properties;
      }
    });
  }

  setUnchanged(element: HTMLDivElement) {
    element.style.backgroundColor = 'rgba(246, 36, 81, 0.5)';
  }

  getPropertyValue(key: any) {
    var value = localStorage.getItem(key);

    if (value) {
      return value;
    } else {
      return this.filtered_properties[key];
    }
  }

  addChangedProperty(key: any, event: Event) {
    const target = event.target as HTMLInputElement;
    const value = target.type === "checkbox" ? target.checked : target.value;
  
    this.changedProperties[key] = value.toString();
    
    if (target.parentElement) {
      this.setUnchanged(target.parentElement as HTMLDivElement);
    }
  }  

  isString(property: any) {
    if (property == "false" || property == "true") {
      return false;  
    } else {
      return true;
    }
  }

  isBoolean(property: any): boolean {
    if (property === 'true') return true;
    if (property === 'false') return true;
    return typeof property === 'boolean';
  }

  saveToLocalStorage(key: any, event: Event) {
    const target = event.target as HTMLInputElement;
    localStorage.setItem(key, target.value);
  }

  convertBoolean(bool: any): boolean {
    if (bool === 'true') return true;
    if (bool === 'false') return false;
    return typeof bool === 'boolean';
  }

  toBoolean(key:any, property: any): boolean {
    var value = this.changedProperties[key];
    if (key in this.changedProperties) return this.convertBoolean(value);
    if (property === 'true') return true;
    if (property === 'false') return false;
    return typeof property === 'boolean';
  }

  filterProperties() {
    console.log(this.search_query);
    console.log("filtering");
    this.filtered_properties = Object.fromEntries(
      Object.entries(this.properties).filter(([key, value]) => 
        key.toLowerCase().includes(this.search_query.toLowerCase())
      )
    );
    
    Object.keys(localStorage).forEach(key => {
      var div = document.getElementById(key) as HTMLDivElement
      if (div) {
        console.log(div);
        this.setUnchanged(div);
      }
    }); 
  }

  saveProperties() {
    var url = this.config.buildUrl("update_server_properties") + `?id=${this.server_id}&updated_properties=${JSON.stringify(this.changedProperties)}`

    this.changedProperties = {};

    this.http.get(url).subscribe((response: any) => {
      console.log(response.message);
      this.setProperties();
    });

    localStorage.clear();
  }

  constructor(private router: Router, private http: HttpClient, private config: ConfigService) {
    const navigation = this.router.getCurrentNavigation();
    this.server = navigation?.extras.state?.['server'] || 'No Data';
    this.server_id = this.server["_id"];
    this.description = this.server["description"];
    this.game_version = this.server.game_version;
  }
}
