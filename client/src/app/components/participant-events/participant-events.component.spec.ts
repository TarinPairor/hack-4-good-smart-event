import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParticipantEventsComponent } from './participant-events.component';

describe('ParticipantEventsComponent', () => {
  let component: ParticipantEventsComponent;
  let fixture: ComponentFixture<ParticipantEventsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ParticipantEventsComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(ParticipantEventsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
