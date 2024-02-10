import { Event } from './event.models';
import { Question } from './question.models';

export interface Survey {
  id: number;
  name: string;
  admin: string;
  event: Event | null;
  description: string;
  questions: Question[];
}
