import {
    HttpClient,
    HttpClientModule,
    HttpRequest,
  } from '@angular/common/http';
  import { Component, OnInit } from '@angular/core';
  import { ActivatedRoute, RouterOutlet } from '@angular/router';
  import { ConfigService } from '../config.service';
  import { CommonModule } from '@angular/common';
  import { ServerPageLeftComponent } from '../server-page-left/server-page-left.component';
  
  @Component({
    selector: 'app-server-page',
    standalone: true,
    imports: [
      RouterOutlet,
      HttpClientModule,
      CommonModule,
      ServerPageLeftComponent,
    ],
    templateUrl: './server-page.component.html',
    styleUrl: './server-page.component.css',
  })
  export class ServerPageComponent implements OnInit {
    private server: any = {};
    protected serverId: string | null = null;
    protected endpoint: string | null = null;
    protected game_version: string | null = null;
    protected server_version: string | null = null;
    protected adress: string | null = null;
    protected ram_min: string | null = null;
    protected ram_max: string | null = null;
    private serverStarted: boolean = false;
  
    //WHEN LAUNCHING, CHECK IF SERVER IS STARTED
  
    ngOnInit(): void {
      this.serverId = this.route.snapshot.paramMap.get('id');
      this.endpoint = `/server/${this.serverId}`;
      var url = this.config.buildUrl('get_server') + `?id=${this.serverId}`;
      this.http.get(url).subscribe((response: any) => {
        this.server = JSON.parse(response?.data ?? response);
        console.log('Fetched Server:', this.server);
        this.isServerStarted();
      });
    }
  
    isServerStarted(): void {
      var url =
        this.config.buildUrl('is_server_started') + `?id=${this.serverId}`;
      this.http.get(url).subscribe((response: any) => {
        console.log(response.data)
        if (response.data == 'true') {
          this.serverStarted = true;
        } else {
          this.serverStarted = false;
        }
        
        this.setStartButton(this.serverStarted);
        this.handleStatus();
        this.handleInformations();
      });
    }
  
    handleInformations() {
      this.game_version = this.server['game_version'];
      this.server_version = this.server['server_version'];
      this.ram_max = this.server['ram_max'];
      this.ram_min = this.server['ram_min'];
      this.adress = 'temporary.adress:50000';
    }
  
    handleStatus() {
      const status_text = document.getElementById(
        'text-status'
      ) as HTMLHeadElement;
      const status_box = document.getElementById('status-box') as HTMLDivElement;
  
      if (!this.serverStarted) {
        status_text.innerHTML = 'Offline';
        status_box.style.backgroundColor = 'red';
      } else {
        status_text.innerHTML = 'Online';
        status_box.style.backgroundColor = '#1dc682';
      }
    }
  
    setStartButton(status: boolean) {
      const button = document.getElementById('start-button') as HTMLButtonElement;
      button.disabled = false;
      if (status) {
        button.innerHTML = 'Stop';
        button.style.backgroundColor = 'red';
      } else {
        button.innerHTML = 'Démarrer';
        button.style.backgroundColor = '#1dc682';
      }
    }
    
    setButtonOnHold() {
      const button = document.getElementById('start-button') as HTMLButtonElement;
      button.style.backgroundColor = "gray";
      button.innerHTML = "Wait..";
      button.disabled = true;
    }

    handleStartButton() {
      const button = document.getElementById('start-button') as HTMLButtonElement;
      this.setButtonOnHold();

      if (!this.serverStarted) {
        this.serverStarted = true;
    
        var url = this.config.buildUrl('start_server') + `?id=${this.serverId}`;
        this.http.get(url).subscribe((response: any) => {
          console.log('Starting server');
          var message = response.message;
          if (message == "success") {
            this.setStartButton(this.serverStarted);
          }
        });
      } else {
        this.serverStarted = false;
    
        var url = this.config.buildUrl('stop_server') + `?id=${this.serverId}`;
        this.http.get(url).subscribe((response: any) => {
          console.log('Stopping server');
          var message = response.message;
          if (message == "success") {
            this.setStartButton(this.serverStarted);
          }
        });
      }
  
      this.handleStatus();
    }
  
    startServer(event: Event): void {
      console.log(this.serverStarted);
      this.handleStartButton();
    }
  
    constructor(
      private http: HttpClient,
      private config: ConfigService,
      private route: ActivatedRoute
    ) {}
  }
  