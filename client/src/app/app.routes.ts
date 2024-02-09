import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { AdminEventsComponent } from './components/admin-events/admin-events.component';
import { ParticipantEventsComponent } from './components/participant-events/participant-events.component';
import { EventParticipationComponent } from './components/event-participation/event-participation.component';

export const routes: Routes = [
  {
    path: 'login',
    component: LoginComponent,
  },
  {
    path: 'signup',
    component: SignupComponent,
  },
  {
    path: 'admin-events',
    component: AdminEventsComponent,
  },
  {
    path: 'participant-events',
    component: ParticipantEventsComponent,
  },
  {
    path: 'participant-events/:event_id',
    component: EventParticipationComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
