import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { AdminEventsComponent } from './components/admin-events/admin-events.component';
import { ParticipantEventsComponent } from './components/participant-events/participant-events.component';
import { EventParticipationComponent } from './components/event-participation/event-participation.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { AppComponent } from './app.component';
import { HomepageComponent } from './components/homepage/homepage.component';

export const routes: Routes = [
  {
    path: '',
    component: HomepageComponent,
  },
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
    path: 'admin-events/:event_id',
    component: DashboardComponent,
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
