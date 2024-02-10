import { Event } from './event.models';

export interface Attendance {
  event: Event;
  participant: string;
  check_in_time: string;
  check_out_time: string | null;
  is_present: boolean;
}
