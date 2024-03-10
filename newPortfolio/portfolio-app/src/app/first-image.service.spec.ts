import { TestBed } from '@angular/core/testing';

import { FirstImageService } from './first-image.service';

describe('FirstImageService', () => {
  let service: FirstImageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FirstImageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
