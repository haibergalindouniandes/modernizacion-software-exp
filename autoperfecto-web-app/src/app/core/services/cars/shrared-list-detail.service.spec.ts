import { TestBed } from '@angular/core/testing';

import { ShraredListDetailService } from './shrared-list-detail.service';

describe('ShraredListDetailService', () => {
  let service: ShraredListDetailService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ShraredListDetailService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
