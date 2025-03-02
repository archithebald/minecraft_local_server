import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServerFilesPageComponent } from './server-files-page.component';

describe('ServerFilesPageComponent', () => {
  let component: ServerFilesPageComponent;
  let fixture: ComponentFixture<ServerFilesPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ServerFilesPageComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ServerFilesPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
